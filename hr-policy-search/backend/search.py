def search_policies(policies, keyword):
    q = keyword.strip().lower()

    if q == "":
        return policies

    return [
        policy
        for policy in policies
        if q in policy["title"].lower() or q in policy["category"].lower()
    ]
