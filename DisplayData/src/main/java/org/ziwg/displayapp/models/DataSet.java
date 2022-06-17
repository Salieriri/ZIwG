package org.ziwg.displayapp.models;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.Setter;

import java.util.List;

@AllArgsConstructor
@Getter
@Setter
public class DataSet {

    private List<Node> nodes;
    private List<Edge> edges;

    @AllArgsConstructor
    @Getter
    @Setter
    public static class Node {
        private Integer id;
        private String label;
        private String title;
    }

    @AllArgsConstructor
    @Getter
    @Setter
    public static class Edge {
        private Integer from;
        private Integer to;
    }
}
