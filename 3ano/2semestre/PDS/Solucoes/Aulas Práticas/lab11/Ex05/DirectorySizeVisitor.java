package lab11.Ex05;

import java.io.IOException;
import java.nio.file.*;
import java.nio.file.attribute.BasicFileAttributes;
import java.util.concurrent.atomic.AtomicLong;

public class DirectorySizeVisitor {

    private final String directoryPath;
    private final boolean recursive;

    public DirectorySizeVisitor(String directoryPath, boolean recursive) {
        this.directoryPath = directoryPath;
        this.recursive = recursive;
        calculateDirectorySize();
    }

    private void calculateDirectorySize() {
        AtomicLong totalSize = new AtomicLong(0);

        try {
            Path rootPath = Paths.get(directoryPath);

            Files.walkFileTree(rootPath, new SimpleFileVisitor<Path>() {

                @Override
                public FileVisitResult preVisitDirectory(Path dir, BasicFileAttributes attrs) throws IOException {
                    if (!recursive && !rootPath.equals(dir)) {
                        return FileVisitResult.SKIP_SUBTREE;
                    }
                    return FileVisitResult.CONTINUE;
                }

                @Override
                public FileVisitResult visitFile(Path file, BasicFileAttributes attrs) throws IOException {
                    long fileSize = attrs.size();
                    totalSize.addAndGet(fileSize);
                    System.out.println(file.getFileName() + ": " + fileSize + " kB");
                    return FileVisitResult.CONTINUE;
                }

                @Override
                public FileVisitResult postVisitDirectory(Path dir, IOException exc) throws IOException {
                    if (rootPath.equals(dir)) {
                        System.out.println("Total: " + totalSize.get() + " kB");
                    }
                    return FileVisitResult.CONTINUE;
                }

            });
        } catch (IOException e) {
            System.err.println("Error: " + e.getMessage());
            System.exit(0);
        }
    }
}
