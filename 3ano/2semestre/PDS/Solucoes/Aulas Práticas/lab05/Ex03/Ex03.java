package lab05.Ex03;

import java.util.List;

public class Ex03 {
    public static void main(String[] args) {
        Movie movie = new Movie.Movie_Builder("The Matrix", 1999)
                .director(new Person("Lana Wachowski"))
                .writer(new Person("Lilly Wachowski"))
                .cast(List.of(new Person("Keanu Reeves"), new Person("Laurence Fishburne")))
                .locations(List.of(new Place("San Francisco"), new Place("Los Angeles")))
                .languages(null)
                .isIndependent(false)
                .isNetflix(false)
                .isTelevision(false)
                .build();

        System.out.println(movie);
    }
}
