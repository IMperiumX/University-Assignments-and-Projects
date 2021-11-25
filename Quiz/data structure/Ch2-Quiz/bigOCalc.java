public class bigOCalc {
    int f(int n, int[] a) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                for (int k = 0; k < n; k++) {
                    if (i != j && j != k && i != k) {
                        if (a[i] == a[j] && a[j] == a[k])
                            return 1;
                    }
                }
            }
            return 0;
        }
    }
}