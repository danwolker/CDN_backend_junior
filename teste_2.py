import requests
import os  
from dotenv import load_dotenv  

# Carregar API Key do arquivo .env
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
    return [(movie["id"], movie["title"]) for movie in data.get("results", [])[:10]]

def get_movie_details(movie_id):
    url = f"{BASE_URL}/movie/{movie_id}?api_key={API_KEY}&language=en-US"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"ERRO: Não foi possível buscar detalhes do filme ID {movie_id}.")
        return None

    data = response.json()
    title = data.get("title", "Título Desconhecido")
    genres = [genre["id"] for genre in data.get("genres", [])]
    return title, genres

def get_recommendations_by_genre(genres):
    genre_str = ",".join(map(str, genres))
    url = f"{BASE_URL}/discover/movie?api_key={API_KEY}&language=en-US&with_genres={genre_str}&sort_by=popularity.desc"
    response = requests.get(url)

    if response.status_code != 200:
        print("ERRO: Não foi possível buscar filmes recomendados por gênero.")
        return []

    data = response.json()
    return [(movie["id"], movie["title"]) for movie in data.get("results", [])[:5]]

if __name__ == "__main__":

    popular_movies = get_popular_movies()

    if not popular_movies:
        print("Não foi possível buscar filmes populares. Encerrando o programa.")
        exit()

    print("\n🎬 **Filmes Populares:**")
    for movie_id, title in popular_movies:
        print(f"  - {title} (ID: {movie_id})")

    movie_id = input("\nDigite o ID de um dos filmes para ver recomendações: ").strip()

    try:
        movie_id = int(movie_id)
    except ValueError:
        print("ERRO: O ID do filme deve ser um número inteiro válido.")
        exit()

    movie_details = get_movie_details(movie_id)

    if not movie_details:
        print("Não foi possível encontrar detalhes para esse filme.")
        exit()

    movie_title, movie_genres = movie_details

    print(f"\n🎥 Você escolheu: **{movie_title}**")


    recommendations = get_recommendations_by_genre(movie_genres)

    if recommendations:
        print("**Filmes recomendados com base no gênero de", movie_title, ":**")
        for movie in recommendations:
            print(f"- {movie[1]} (ID: {movie[0]})")
    else:
        print("Nenhuma recomendação disponível para este filme.")
