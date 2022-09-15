import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;

public class App{
    public static void main(String[] args) throws IOException{
        String[] input = parseInput();
        System.out.println(partOne(input));
        System.out.println(partTwo(input));
    }

    private static String[] parseInput() throws IOException {
        return Files.lines(Paths.get("./input.txt"))
        .map(String::valueOf)
        .toArray(String[]::new);
    }

    private static Integer partOne (String[] input){
        Integer h_pos = 0;
        Integer d_pos = 0;
        for(String delta: input){
            String[] parsedDelta = delta.split(" ");
            if(parsedDelta[0].equals("forward")){
                h_pos = h_pos + Integer.parseInt(parsedDelta[1]);
            } 
            else if(parsedDelta[0].equals("down")){
                d_pos = d_pos + Integer.parseInt(parsedDelta[1]);
            } else {
                d_pos = d_pos - Integer.parseInt(parsedDelta[1]);
            }
        }
        return (h_pos * d_pos);
    }

    private static Integer partTwo(String[] input){
        Integer h_pos = 0;
        Integer d_pos = 0;
        Integer aim = 0;

        for(String delta: input){
            String[] parsedDelta = delta.split(" ");
            if(parsedDelta[0].equals("forward")){
                h_pos = h_pos + Integer.parseInt(parsedDelta[1]);
                d_pos = d_pos + Integer.parseInt(parsedDelta[1]) * aim;
            } 
            else if(parsedDelta[0].equals("down")){
                aim = aim + Integer.parseInt(parsedDelta[1]);
            } else {
                aim = aim - Integer.parseInt(parsedDelta[1]);
            }
        }
        return (h_pos * d_pos);
    }
}