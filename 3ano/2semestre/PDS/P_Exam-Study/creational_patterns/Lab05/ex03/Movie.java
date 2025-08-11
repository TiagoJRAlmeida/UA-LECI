import java.util.ArrayList;
import java.util.List;

public class Movie {
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

   private Movie(Builder builder) {
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


   public static class Builder {
       // Required
       private final String title;
       private final int year;

       // Optional
       private Person director;
       private Person writer;
       private String series;
       private List<Person> cast = new ArrayList<>();
       private List<Place> locations = new ArrayList<>();
       private List<String> languages = new ArrayList<>();
       private List<String> genres = new ArrayList<>();
       private boolean isTelevision;
       private boolean isNetflix;
       private boolean isIndependent;

       public Builder(String title, int year) {
           this.title = title;
           this.year = year;
       }

       public Builder director(Person director) {
           this.director = director;
           return this;
       }

       public Builder writer(Person writer) {
           this.writer = writer;
           return this;
       }

       public Builder series(String series) {
           this.series = series;
           return this;
       }

       public Builder cast(List<Person> cast) {
           this.cast = cast;
           return this;
       }

       public Builder locations(List<Place> locations) {
           this.locations = locations;
           return this;
       }

       public Builder languages(List<String> languages) {
           this.languages = languages;
           return this;
       }

       public Builder genres(List<String> genres) {
           this.genres = genres;
           return this;
       }

       public Builder television(boolean television) {
           this.isTelevision = television;
           return this;
       }

       public Builder netflix(boolean netflix) {
           this.isNetflix = netflix;
           return this;
       }

       public Builder independent(boolean independent) {
           this.isIndependent = independent;
           return this;
       }

       public Movie build() {
           return new Movie(this);
       }
   }
}

