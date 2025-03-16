import java.util.Arrays;

public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!");

        char[][] teste = {{'1', '2', '3'}, {'4', '5', '6'}, {'7', '8', '9'}};

        // for(int i = 0; i < 3; i++){
        //     for(int j = 0; j < 3; j++){
        //         System.out.println(teste[i][j] == '\0');
        //     }
        // }

        System.out.println(teste[1]);
        System.out.println(Arrays.equals(teste[1],new char[]{'4', '5', '6'}));

        System.out.println(teste.length);

        System.out.println(teste[1][2]);
    }
}

// How to run:

// Compile to bytecode: javac HelloWorld.java
// Run the program: java HelloWorld

// Or combine the commands: javac HelloWorld.java && java HelloWorld