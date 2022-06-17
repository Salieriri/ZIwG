package org.ziwg.displayapp.models;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.Setter;

import java.util.ArrayList;

@AllArgsConstructor
@Getter
@Setter
public class SimilarityJson {

    private ArrayList<String> rowlabels;
    private ArrayList<ArrayList<Float>> arr;
}
