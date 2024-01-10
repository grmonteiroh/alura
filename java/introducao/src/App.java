import java.time.LocalDate;

public class App {
    public static void main(String[] args) throws Exception {
        Artigo artigo = new Artigo("Vs Code com Java", new Autor("Junim Ruindade Pura"), 
                            LocalDate.of(2022, 07, 13), Categoria.BACKEND);
        System.out.println(artigo);
    }
}
