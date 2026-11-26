export function searchPolicies(policies, keyword) {
  const q = keyword.trim().toLowerCase();

  if (q === "") {
    return policies;
  }

  return policies.filter(
    (policy) =>
    policy.title.toLowerCase().includes(q) ||
    policy.category.toLowerCase().includes(q)
  );
}