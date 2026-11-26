import { describe, it, expect } from "vitest";
import { searchPolicies } from "./searchPolicies";

const samplePolicies = [
  { id: 1, title: "Annual Leave Policy", category: "Leave" },
  { id: 2, title: "Sick Leave Policy", category: "Leave" },
  { id: 3, title: "Remote Work Policy", category: "Workplace" },
  { id: 4, title: "Code of Conduct", category: "Ethics" },
];

describe("searchPolicies", () => {
  it("returns matching policies for a keyword", () => {
    const result = searchPolicies(samplePolicies, "leave");

    expect(result).toHaveLength(2);
    expect(result.map((p) => p.title)).toEqual([
      "Annual Leave Policy",
      "Sick Leave Policy",
    ]);
  });

  it("returns an empty list for an unknown keyword", () => {
    const result = searchPolicies(samplePolicies, "xyz");

    expect(result).toEqual([]);
  });

  it("returns all policies for an empty search", () => {
    const result = searchPolicies(samplePolicies, "");

    expect(result).toEqual(samplePolicies);
  });

    it("ignores uppercase and lowercase", () => {
    const result = searchPolicies(samplePolicies, "LEAVE");

    expect(result).toHaveLength(2);
  });

  it("ignores spaces around the keyword", () => {
    const result = searchPolicies(samplePolicies, "  remote  ");

    expect(result).toHaveLength(1);
    expect(result[0].title).toBe("Remote Work Policy");
  });

  it("returns all policies when the search is only spaces", () => {
    const result = searchPolicies(samplePolicies, "   ");

    expect(result).toEqual(samplePolicies);
  });

  it("also searches the category", () => {
    const result = searchPolicies(samplePolicies, "ethics");

    expect(result).toHaveLength(1);
    expect(result[0].title).toBe("Code of Conduct");
  });
});