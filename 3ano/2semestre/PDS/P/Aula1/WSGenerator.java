import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;

public class WSGenerator {
    public static void main(String[] args){
        if (args.length < 2 || !args[0].equals("-w")) {
            System.out.println("Usage: java WSGenerator -w <wordlist.txt> [-s <output.txt>]");
            return;
        }

        String inputFile = args[1];
        String outputFile = null;

        if (args.length >= 4 && args[2].equals("-s")) {
            outputFile = args[3];
        }

        WordPlacer wp = new WordPlacer();
        WordSoupFiller wsf = new WordSoupFiller();

        WordSoup soup = new WordSoup();
        Direction direction = null;
        int[] startPosition;

        soup.loadSolutions(inputFile);
        ArrayList<WordLocation> solutions = soup.getSolutions();

        for( WordLocation solution : solutions){
            do{
                startPosition = wp.GenerateStartPosition(soup, solution.getWord());
                direction = wp.GenerateValidDirection(soup, solution.getWord(), startPosition);
            }while(direction == null);

            solution.setColumn(startPosition[0]);
            solution.setRow(startPosition[1]);
            solution.setDirection(direction);
            
            soup = wp.InsertWord(soup, solution);
        }
 
        soup = wsf.FillWS(soup);

        if (outputFile == null ) System.out.println(soup);
        else {
            try (BufferedWriter writer = new BufferedWriter(new FileWriter(outputFile))) {
                writer.write(soup.toString());
            } catch (IOException e) {
                System.out.println("Error writing to file: " + outputFile);
                e.printStackTrace();
            }
        }
    }
}
