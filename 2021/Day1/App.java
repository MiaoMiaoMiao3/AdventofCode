import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;

public class App{
    public static void main(String[] args) throws IOException{
        Integer[] input = parseInput();
        System.out.println(depthIncreaseCount(input));
        System.out.println(filteredDepthIncreaseCount(input));
    }

    private static Integer[] parseInput() throws IOException {
        return Files.lines(Paths.get("./input.txt"))
        .map(Integer::valueOf)
        .toArray(Integer[]::new);
    }

    private static Integer depthIncreaseCount(Integer[] input){
        Integer baseline = null;
        Integer increaseCount = 0;
        for(Integer depth: input){
            if (baseline == null){
                baseline = depth;
            } else {
                if (depth > baseline){
                    increaseCount = increaseCount + 1;
                }
            }
            baseline = depth;
        }
        return increaseCount;
    }

    private static Integer filteredDepthIncreaseCount(Integer[] input){
        Integer pointer1 = null;
        Integer pointer2 = null;
        Integer counter = 0;

        for(int depth = 0; depth +3 <= input.length-1; depth++){
            pointer1 = input[depth];
            pointer2 = input[depth+3];
            if (pointer1 < pointer2){
                counter +=1;
            }
        }
        return counter;
    }
}