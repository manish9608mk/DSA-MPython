# Pattern Cheat Sheet: clue → technique → folder → example → trap

Read the question, find the **clue words**, pick the technique, then open the folder for the template.

| Clue in the question | Technique | Folder | Example (LeetCode) | Common trap |
|---|---|---|---|---|
| sorted array, pair/triplet with a sum | two pointers, opposite ends | 06 | 167, 15 | forgetting to skip duplicates (3Sum) |
| in-place remove / move / partition | slow-fast (write pointer) | 06 | 26, 283 | `slow` vs `slow + 1` as the returned length |
| contiguous subarray/substring, longest or shortest with a condition | sliding window | 07 | 3, 209, 76 | negatives break it; `if` instead of `while` |
| "exactly K" subarrays | atMost(K) − atMost(K−1) | 07 | 992 | direct window is not monotonic |
| many range sums; subarray sum = k (negatives) | prefix sum + hash map | 08, 04 | 560, 525 | missing `{0: 1}` |
| many range updates | difference array | 08 | 1109, 1094 | array size `n`, not `n + 1` |
| sorted data; first/last position; insert position | binary search, lower/upper bound | 09 | 34, 35 | `hi = mid - 1` in the first-True template |
| "minimum X such that feasible" / "maximum of the minimum" | binary search on the answer | 09 | 875, 1011, 410 | wrong answer range; lower mid in maximize |
| all arrangements / all subsets | backtracking (choose, explore, undo) | 16 | 78, 46, 39 | saving `path` instead of `path[:]` |
| smaller copy of itself; trees | recursion | 10, 14 | 104, 226 | no base case; slicing in recursion |
| duplicates, frequency, complement | hash set / map / Counter | 04 | 217, 1, 242 | using `list` as a dict key |
| group by "shape" | hash with a signature key | 04 | 49 | sorting each word when a count tuple is enough |
| next greater/smaller, histogram, brackets | stack / monotonic stack | 12 | 739, 84, 20 | storing values instead of indexes |
| window maximum, level order, BFS | queue / deque | 13 | 239, 102 | `list.pop(0)` (O(n)) |
| tree height / path / diameter / LCA | DFS bottom-up (+ global answer) | 14 | 543, 236, 124 | node with one child is not a leaf |
| level by level, views, width | BFS on trees | 13, 14 | 199, 103 | no level-size loop |
| BST: k-th, validate, range | inorder, `(lo, hi)` range | 14 | 230, 98 | validating only parent-child |
| k largest / smallest / top-k frequent | heap of size k | 15 | 215, 347 | wrong heap type (use min-heap for k largest) |
| median of a stream | two heaps | 15 | 295 | unbalanced sizes |
| merge k sorted | heap of heads | 15 | 23 | pushing the whole input |
| prefix queries, autocomplete, words in a grid | trie | 17 | 208, 212 | forgetting `is_end` |
| intervals: merge / insert / overlap | sort by start | 18 | 56, 57 | `<` vs `<=` on touching ends |
| intervals: max non-overlapping, min arrows | sort by end (greedy) | 18 | 435, 452 | sorting by start |
| local best choice is provable | greedy | 18 | 55, 134, 763 | no counterexample check |
| odd one out, XOR, power of two, subsets (n ≤ 20) | bit manipulation | 19 | 136, 191 | precedence: `(n & 1) == 0` |
| components, islands, reachability | DFS / BFS / Union-Find | 20 | 200, 547 | no `visited`; reversed edge direction |
| fewest steps (unweighted), multi-source | BFS | 13, 20 | 994, 286 | marking visited on pop |
| shortest path, non-negative weights | Dijkstra | 20 | 743, 1631 | using it with negative edges |
| negative weights, at most K edges | Bellman-Ford | 20 | 787 | forgetting the copy per round |
| prerequisites, ordering, directed cycle | topological sort | 20 | 207, 210 | direction of `[a, b]` |
| connect everything cheapest | MST (Kruskal / Prim) | 20 | 1584 | confusing it with shortest path |
| count ways / min / max with repeated subproblems | dynamic programming | 21 | 70, 322, 300 | state not defined in words |
| subset sum / partition / capacity | knapsack DP | 21 | 416, 494 | wrong loop direction (once vs reuse) |
| two strings: LCS, edit distance | 2D DP | 21 | 1143, 72 | off-by-one in `dp[i][j]` |
| grid paths, minimum path sum | grid DP | 21 | 62, 64 | first row/column base cases |
| buy/sell with states | state-machine DP | 21 | 309, 188 | updating states with today's value |
| range query + point update | Fenwick / segment tree | 22 | 307, 315 | 0-based Fenwick |
| primes, gcd, mod 10⁹+7, nCr | math / modular arithmetic | 23 | 204, 50 | `%` only at the end |
| O(1) get/put, LRU/LFU, rate limiter | hash map + linked list / heap / deque | 24 | 146, 460, 380 | forgetting the key in the node |

## Decision flow when you are stuck

1. Can I **sort** it? Does it become easy?
2. Is it **contiguous** (window / prefix) or **sorted** (two pointers, binary search)?
3. Can a **hash** remove the inner loop?
4. Is there a **monotonic** feasibility rule (binary search on the answer)?
5. Is it a **graph** in disguise (nodes, edges, dependencies, grid)?
6. Does the same subproblem repeat (**DP**)? Do I need **all** solutions (**backtracking**)?
7. Is a local choice provably best (**greedy**)?
8. Still stuck: write the brute force, then ask "what is repeated work?"

## Constraint hints

| n | Complexity |
|---|---|
| ≤ 10 | O(n!) |
| ≤ 20 | O(2ⁿ · n), bitmask |
| ≤ 500 | O(n³) |
| ≤ 5000 | O(n²) |
| ≤ 10⁵ | O(n log n) |
| ≤ 10⁶ | O(n) |
| up to 10⁹ | O(log n) or O(√n) |
