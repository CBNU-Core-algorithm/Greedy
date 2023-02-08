import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.util.*;
import java.lang.Math;
public class 세탁소사장동혁 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine());
        int C[] = new int[T];
        int Q[] = new int[T];
        int D[] = new int[T];
        int N[] = new int[T];
        int P[] = new int[T];

        for(int i = 0; i < T ; i++) {
            C[i] = Integer.parseInt(br.readLine());

            Q[i] = C[i] / 25;
            C[i] %= 25;
            D[i] = C[i] / 10;
            C[i] %= 10;
            N[i] = C[i] / 5;
            C[i] %= 5;
            P[i] = C[i];
        }

        for (int j = 0; j < T ; j++){
            System.out.println(Q[j]+" "+D[j]+" "+N[j]+" "+P[j]);
        }
    }
}
