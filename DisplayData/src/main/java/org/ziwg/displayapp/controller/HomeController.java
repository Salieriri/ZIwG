package org.ziwg.displayapp.controller;

import com.google.gson.Gson;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.util.StringUtils;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;
import org.ziwg.displayapp.models.DataSet;
import org.ziwg.displayapp.models.SimilarityJson;

import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.Reader;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardCopyOption;
import java.util.ArrayList;
import java.util.Enumeration;
import java.util.List;
import java.util.Objects;
import java.util.zip.ZipEntry;
import java.util.zip.ZipFile;

@Controller
public class HomeController {

    private final String UPLOAD_DIR = "./uploads/";

    @GetMapping
    public String home(final Model model) {
        return "home";
    }

    @PostMapping("/upload")
    public String uploadFile(@RequestParam("file") MultipartFile file, RedirectAttributes attributes) {

        // check if file is empty
        if (file.isEmpty()) {
            attributes.addFlashAttribute("message", "Please select a file to upload.");
            return "redirect:/";
        }

        // normalize the file path
        final String fileName = StringUtils.cleanPath(Objects.requireNonNull(file.getOriginalFilename()));

        // save the file on the local file system
        try {
            final Path path = Paths.get(UPLOAD_DIR + fileName);
            Files.copy(file.getInputStream(), path, StandardCopyOption.REPLACE_EXISTING);
            final DataSet dataSet = similarityJsonToDataSet(Objects.requireNonNull(readZip(path)));
            attributes.addFlashAttribute("dataSet", dataSet);

        } catch (IOException e) {
            e.printStackTrace();
        }

        // return success response
        attributes.addFlashAttribute("message", "Plik został pomyślnie wysłany " + fileName + '!');

        return "redirect:/";
    }

    private SimilarityJson readZip(final Path path) {

        try (final ZipFile zipFile = new ZipFile(path.toFile())) {
            final Enumeration<? extends ZipEntry> entries = zipFile.entries();

            while (entries.hasMoreElements()) {
                ZipEntry entry = entries.nextElement();
                if (entry.getName().contains("similarity")) {
                    final InputStream stream = zipFile.getInputStream(entry);
                    final Reader reader = new InputStreamReader(stream, StandardCharsets.UTF_8);
                    return new Gson().fromJson(reader, SimilarityJson.class);
                }
            }
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
        return null;
    }

    private DataSet similarityJsonToDataSet(final SimilarityJson similarity) {
        final List<DataSet.Edge> edges = new ArrayList<>();
        final List<DataSet.Node> nodes = new ArrayList<>();

        final ArrayList<String> rowlabels = similarity.getRowlabels();
        for (int i = 0; i < rowlabels.size(); i++) {
            final String label = rowlabels.get(i);
            nodes.add(new DataSet.Node(i, "", label));
        }

        final ArrayList<ArrayList<Float>> arrays = similarity.getArr();
        for (int i = 0; i < arrays.size(); i++) {
            for (int j = i + 1; j < arrays.get(i).size(); j++) {
                if (arrays.get(i).get(j) > 0.3) {
                    edges.add(new DataSet.Edge(i, j));
                }
            }
        }

        return new DataSet(nodes, edges);
    }

}
