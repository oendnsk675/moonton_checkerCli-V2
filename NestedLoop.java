package Perulangan;

public class NestedLoop {
    public static void main(String[] args) {
        
        int Nilai = 5;
        
        for (int i = Nilai; i >= 1; i--) {
            for (int j = Nilai; j >= i; j--) {
                System.out.print(j);
            }
            System.out.println("");
        }
        
        for (int i = 2; i <= Nilai; i++) {
            for (int j = Nilai; j >= i; j--) {
                System.out.print(j);
            }
            System.out.println("");
        }

    }
}
