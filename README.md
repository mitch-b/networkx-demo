# NetworkX Demo

For learning purposes. Try in Codespaces!

## Proof of Concept Thoughts

- [x] Open repo & run
- [x] Use NetworkX to generate a graph
- [ ] Load graph from file
- [ ] Save graph to file
- [x] Provide visual endpoints to view subgraphs
- [ ] Investigate more graph visualization options
- [ ] Business rule engine for traversal rules

## Installation (Docker)

```bash
docker build -t networkx-demo .
docker run --rm -p 8081:8080 networkx-demo

curl http://localhost:8081/hello/world
curl http://localhost:8081/graph/paths/D/to/F
```

## Notes

* https://networkx.org/documentation/stable/auto_examples/index.html
