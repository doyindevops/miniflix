from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="MiniFlix Catalog API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MOVIES = [
    {"id": 1, "title": "Night Shift Lagos", "year": 2024, "genre": "Drama"},
    {"id": 2, "title": "K8s Kingdom", "year": 2023, "genre": "Tech"},
    {"id": 3, "title": "GitOps: The Movie", "year": 2025, "genre": "Thriller"},
    {"id": 4, "title": "Ingress Wars", "year": 2022, "genre": "Action"},
    {"id": 5, "title": "Pods & Promises", "year": 2021, "genre": "Comedy"},
    {"id": 6, "title": "ArgoCD City", "year": 2024, "genre": "Sci-Fi"},
    {"id": 7, "title": "Docker Nights", "year": 2020, "genre": "Drama"},
    {"id": 8, "title": "Cluster Ready", "year": 2025, "genre": "Tech"},
    {"id": 9, "title": "Load Balancer Legends", "year": 2023, "genre": "Fantasy"},
    {"id": 10, "title": "SRE Stories", "year": 2022, "genre": "Documentary"},
]

@app.get("/health")
def health():
    return {"ok": True}

@app.get("/movies")
def list_movies(q: str | None = None):
    if not q:
        return MOVIES
    qlow = q.lower()
    return [m for m in MOVIES if qlow in m["title"].lower() or qlow in m["genre"].lower()]

@app.get("/movies/{movie_id}")
def get_movie(movie_id: int):
    for m in MOVIES:
        if m["id"] == movie_id:
            return m
    return {"error": "not_found", "id": movie_id}
