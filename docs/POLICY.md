# Repository hygiene policy
1. Branches fully merged into `main` are deleted from the remote after merge.
2. Unmerged branches are never deleted by automation; they are listed for the owner.
3. Draft releases whose notes mark them as superseded are deleted. Published releases are never deleted.
4. Tags with no matching published release are reported, not removed.
5. `main` requires a pull request with at least one approval and passing `ci` before merge.
