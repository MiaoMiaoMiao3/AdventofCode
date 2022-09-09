package Day1;


import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;

public class App{
    public void main(String[] args) throws IOException{
        String [] input = parseInput();
        System.out.println(input);
    }

    private static String[] parseInput() throws IOException {
        return Files.lines(Paths.get("./Input.txt"))
        .map(String::valueOf)
        .toArray(String[]::new);
    }
}