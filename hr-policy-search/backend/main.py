from fastapi import FastAPI, HTTPException

from data import POLICIES
from search import search_policies

app = FastAPI(title="HR Policy Search API")


@app.get("/")
def root():
    return {"message": "HR Policy Search API"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/policies")
def list_policies(q: str = "", category: str | None = None):
    policies = POLICIES

    if category:
        policies = [
            policy
            for policy in policies
            if policy["category"].lower() == category.lower()
        ]

    return search_policies(policies, q)


@app.get("/policies/{policy_id}")
def get_policy(policy_id: int):
    for policy in POLICIES:
        if policy["id"] == policy_id:
            return policy
    raise HTTPException(status_code=404, detail="Policy not found")
