# dev-team-e2e-scratch

A trivial scratch app used to end-to-end test the `dev-team` autonomous
delivery pipeline. Not a real product.

`app.py` exposes an `add(a, b)` function, tested with `unittest` in
`test_app.py`, and exercised by CI on every push and pull request.
