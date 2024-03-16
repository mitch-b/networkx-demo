# NetworkX Demo

For learning purposes. Try in Codespaces!

## Proof of Concept Thoughts

- [ ] Open repo & run
- [ ] Use NetworkX to generate a graph
- [ ] Load graph from file
- [ ] Save graph to file
- [ ] Use FastAPI to serve the graph
- [ ] Provide visual endpoints to view subgraphs
- [ ] Investigate more graph visualization options
- [ ] Business rule engine for traversal rules

## Installation (Docker)

```bash
docker build -t networkx-demo .
docker run --rm -p 8081:8080 networkx-demo

curl http://localhost:8081/hello/world
```

## Notes

* https://networkx.org/documentation/stable/auto_examples/index.html
* https://stackoverflow.com/questions/75185806/how-to-serve-a-pyvis-graph-with-fastapi
* https://stackoverflow.com/questions/65296604/how-to-return-a-htmlresponse-with-fastapi
