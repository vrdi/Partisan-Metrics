import json
import csv
import numpy as np

from gerrychain import Graph

def most_rep_districts(json, num_dists, election, D):
    graph = Graph.from_json("./"+json+".json")

    TOTPOP = "TOTPOP"
    DEMVOTE = election+"D"
    REPVOTE = election+"R"

    # Ensure data are integers
    if election != "PRES16":
        for n in graph.nodes:
            if type(graph.nodes[n][DEMVOTE]) != int:
                graph.nodes[n][DEMVOTE] = int(graph.nodes[n][DEMVOTE].replace(",", ""))
            if type(graph.nodes[n][REPVOTE]) != int:
                graph.nodes[n][REPVOTE] = int(graph.nodes[n][REPVOTE].replace(",", ""))

    # Find the ideal population I
    pop_count = 0
    for i in graph.nodes:
        pop_count += graph.nodes[i][TOTPOP]
    pop_count = np.round(pop_count)
    I = (pop_count / num_dists)


    # Create lists of total pop, dem, and rep voters per precinct
    prec_pop = []
    prec_dem = []
    prec_rep = []
    for n in graph.nodes:
        prec_pop.append(graph.nodes[n][TOTPOP])
        prec_rep.append(graph.nodes[n][REPVOTE])
        prec_dem.append(graph.nodes[n][DEMVOTE])


    # Create a sorted list of deltas according to a specific, hard-coded metric

    deltas = []
    for i in range(len(prec_pop)):
        if prec_pop[i] != 0:
            deltas.append([(prec_rep[i] - prec_dem[i]) / prec_pop[i], i])


    rep_deltas = sorted(deltas, reverse = True)
    rep_node_list = []

    # Greedily create precincts
    pop_counter = 0
    for i in range(len(prec_pop)):
        if 0 <= pop_counter < D*I:
            rep_node_list.append(rep_deltas[i][1])
            pop_counter += graph.nodes[rep_deltas[i][1]][TOTPOP]

    dem_votes = 0
    rep_votes = 0
    total_pop = 0


    for m in range(len(rep_node_list)):
        dem_votes += graph.nodes[rep_node_list[m]][DEMVOTE]
        rep_votes += graph.nodes[rep_node_list[m]][REPVOTE]
        total_pop += graph.nodes[rep_node_list[m]][TOTPOP]

    pct = rep_votes / (dem_votes + rep_votes)

    print("For",json,election,":")
    print("The most Republican quasi-district of size",D, "possible is", pct,"Republican")

most_rep_districts("utah", 4, "SEN16", 1)
most_rep_districts("utah", 4, "GOV16", 1)
most_rep_districts("utah", 4, "PRES16", 1)
most_rep_districts("utah", 4, "SEN16", 2)
most_rep_districts("utah", 4, "GOV16", 2)
most_rep_districts("utah", 4, "PRES16", 2)
