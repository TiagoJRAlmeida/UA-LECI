package lab05.Ex03;

import java.util.List;

public class Movie {
    // Atributos
    private final String title;
    private final int year;
    private final Person director;
    private final Person writer;
    private final String series;
    private final List<Person> cast;
    private final List<Place> locations;
    private final List<String> languages;
    private final List<String> genres;
    private final boolean isTelevision;
    private final boolean isNetflix;
    private final boolean isIndependent;

    // Movie Builder
    public static class Movie_Builder {
        // Atributos no Builder
        private String title = null;
        private int year = 0;
        private Person director = null;
        private Person writer = null;
        private String series = null;
        private List<Person> cast = null;
        private List<Place> locations = null;
        private List<String> languages = null;
        private List<String> genres = null;
        private boolean isTelevision = false;
        private boolean isNetflix = false;
        private boolean isIndependent = false;

        // Construtor no Builder
        public Movie_Builder(String title, int year) {
            this.title = title;
            this.year = year;
        }

        // Definir diretor no Builder
        public Movie_Builder director(Person director) {
            this.director = director;
            return this;
        }

        // Definir escritor no Builder
        public Movie_Builder writer(Person writer) {
            this.writer = writer;
            return this;
        }

        // Definir série no Builder
        public Movie_Builder series(String series) {
            this.series = series;
            return this;
        }

        // Definir elenco no Builder
        public Movie_Builder cast(List<Person> cast) {
            this.cast = cast;
            return this;
        }

        // Definir locais no Builder
        public Movie_Builder locations(List<Place> locations) {
            this.locations = locations;
            return this;
        }

        // Definir idiomas no Builder
        public Movie_Builder languages(List<String> languages) {
            this.languages = languages;
            return this;
        }

        // Definir gêneros no Builder
        public Movie_Builder genres(List<String> genres) {
            this.genres = genres;
            return this;
        }

        // Definir se é uma série no Builder
        public Movie_Builder isTelevision(boolean isTelevision) {
            this.isTelevision = isTelevision;
            return this;
        }

        // Definir se está no Netflix no Builder
        public Movie_Builder isNetflix(boolean isNetflix) {
            this.isNetflix = isNetflix;
            return this;
        }

        // Definir se é independente no Builder
        public Movie_Builder isIndependent(boolean isIndependent) {
            this.isIndependent = isIndependent;
            return this;
        }

        // Construir objeto Movie
        public Movie build() {
            return new Movie(this);
        }
    }

    // Construtor privado do Movie através do Movie_Builder
    private Movie(Movie_Builder builder) {
        this.title = builder.title;
        this.year = builder.year;
        this.director = builder.director;
        this.writer = builder.writer;
        this.series = builder.series;
        this.cast = builder.cast;
        this.locations = builder.locations;
        this.languages = builder.languages;
        this.genres = builder.genres;
        this.isTelevision = builder.isTelevision;
        this.isNetflix = builder.isNetflix;
        this.isIndependent = builder.isIndependent;
    }

    // Método toString
    public String toString() {
        // return tostring of all fields
        return "Title: " + title + "\n" +
                "Year: " + year + "\n" +
                "Director: " + director + "\n" +
                "Writer: " + writer + "\n" +
                "Series: " + series + "\n" +
                "Cast: " + cast + "\n" +
                "Locations: " + locations + "\n" +
                "Languages: " + languages + "\n" +
                "Genres: " + genres + "\n" +
                "Is Television: " + isTelevision + "\n" +
                "Is Netflix: " + isNetflix + "\n" +
                "Is Independent: " + isIndependent + "\n";
    }
}
