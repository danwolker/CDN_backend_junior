import requests
import json
import os
from collections import Counter
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("TMDB_API_KEY")
BASE_URL = "https://api.themoviedb.org/3"

def get_popular_movies():
    url = f"{BASE_URL}/movie/popular?api_key={API_KEY}&language=en-US&page=1"
    response = requests.get(url)

    if response.status_code != 200:
        print("ERRO: Não foi possível buscar os filmes populares.")
        return []

    data = response.json()
    return [(movie["id"], movie["title"]) for movie in data.get("results", [])[:5]] 

def get_movie_details(movie_id):
    url = f"{BASE_URL}/movie/{movie_id}?api_key={API_KEY}&append_to_response=credits"
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"ERRO: Não foi possível buscar o filme ID {movie_id}.")
        return None

    return response.json()

def process_movies(movie_ids):
    actors_count = Counter()
    genres_count = Counter()
    actor_revenue = {}

    for movie_id in movie_ids:
        movie = get_movie_details(movie_id)
        if not movie:
            continue

        for genre in movie.get("genres", []):
            genres_count[genre["name"]] += 1

        revenue = movie.get("revenue", 0) 
        for actor in movie.get("credits", {}).get("cast", [])[:10]: 
            actors_count[actor["name"]] += 1
            actor_revenue[actor["name"]] = actor_revenue.get(actor["name"], 0) + revenue

    top_5_actors = sorted(actor_revenue.items(), key=lambda x: x[1], reverse=True)[:5]

    report = {
        "participacao_atores": dict(actors_count),
        "frequencia_generos": dict(genres_count),
        "top_5_atores_bilheteria": top_5_actors
    }

    with open("relatorio_filmes.json", "w", encoding="utf-8") as file:
        json.dump(report, file, indent=4, ensure_ascii=False)

    print("**Análise de Filmes**")
    print("Participação por Ator:")
    for actor, count in actors_count.most_common(10):
        print(f"  - {actor}: {count} filmes")

    print("Frequência de Gêneros:")
    for genre, count in genres_count.items():
        print(f"  - {genre}: {count} filmes")

    print("**Top 5 Atores com Maior Bilheteria**:")
    for actor, revenue in top_5_actors:
        print(f"  - {actor}: ${revenue:,}")

    print("Relatório salvo como 'relatorio_filmes.json'!")

if __name__ == "__main__":
    popular_movies = get_popular_movies()

    if not popular_movies:
        print("Não foi possível buscar filmes populares. Encerrando o programa.")
        exit()

    print("**Filmes Populares:**")
    for movie_id, title in popular_movies:
        print(f"  - {title} (ID: {movie_id})")

    movie_ids = input("Digite os IDs dos filmes para análise, separados por vírgula: ").split(",")
    process_movies([id.strip() for id in movie_ids])
