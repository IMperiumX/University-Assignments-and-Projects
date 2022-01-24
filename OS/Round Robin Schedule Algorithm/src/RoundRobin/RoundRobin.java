import java.util.Scanner;

/*Round Robin (RR) algorithm is a CPU scheduling algorithm. It is also used in network
schedulers. It is especially designed for time sharing system. It is also known as time slicing
scheduling algorithm. It is closely similar to FCFS scheduling. In this section, we will discuss the
round robin scheduling algorithm and its implementation in a Java program.
*/
public class RoundRobin {
    public static void main(String[] args) {
        try (Scanner user_input = new Scanner(System.in)) {
            System.out.println("Welcome to Our RR CPU Schedual Programming");
            System.out.println("------------------------------------------");
            System.out.print("Please, Enter number of process :  ");

            int ProcessIndex;

            int ProcessNumber = user_input.nextInt();

            // Burst Time: Burst time is the total time taken by the process for its execution on the CPU.
            int[] BurstTime = new int[ProcessNumber];
            int[] Rem_BurstTime = new int[ProcessNumber];

            for (ProcessIndex = 0; ProcessIndex < ProcessNumber; ProcessIndex++) {
                System.out.print("Enter burst Time for Process\t" + (ProcessIndex + 1) + ("   :"));
                BurstTime[ProcessIndex] = user_input.nextInt();
                Rem_BurstTime[ProcessIndex] = BurstTime[ProcessIndex];
            }

            int ProcessCount;
            int temp, sq = 0;

            System.out.print("Enter Time quantum :\t");
            int QuantumTime = user_input.nextInt();

            // Turnaround Time: It is an amount of time the process exists in the system.
            // Turnaround Time = Burst Time + Waiting Time
            int[] TurnAroundTime = new int[ProcessNumber];

            do {
                for (ProcessIndex = 0, ProcessCount = 0; ProcessIndex < ProcessNumber; ProcessIndex++) {
                    temp = QuantumTime;
                    if (Rem_BurstTime[ProcessIndex] == 0) {
                        ProcessCount++;
                        continue;
                    }
                    if (Rem_BurstTime[ProcessIndex] > QuantumTime)
                        Rem_BurstTime[ProcessIndex] -= QuantumTime;
                    else if (Rem_BurstTime[ProcessIndex] >= 0) {
                        temp = Rem_BurstTime[ProcessIndex];
                        Rem_BurstTime[ProcessIndex] = 0;
                    }
                    sq += temp;
                    TurnAroundTime[ProcessIndex] = sq;
                }
            } while (ProcessNumber != ProcessCount);

            System.out.println("\nProcess\t\tBurst.T");

            // Waiting Time: It is an amount of time taken by a process for their complete
            // execution. In
            // the time spend by a process in the ready state waiting for CPU.
            // Waiting Time = Turnaround Time - Burst Time
            int[] WaitingTime = new int[ProcessNumber];
            float AvergeWaitingTime = 0;

            // Turnaround Time = Burst Time + Waiting Time
            for (ProcessIndex = 0; ProcessIndex < ProcessNumber; ProcessIndex++) {
                WaitingTime[ProcessIndex] = TurnAroundTime[ProcessIndex] - BurstTime[ProcessIndex];
                AvergeWaitingTime += WaitingTime[ProcessIndex];
                System.out.println("Process " + (ProcessIndex + 1) + "  \t  " + BurstTime[ProcessIndex]);
            }
            AvergeWaitingTime /= ProcessNumber;

            System.out.println("The Average Waiting Time = " + AvergeWaitingTime);
        } catch (Exception InputMismatchException) {
            System.out.println("Try Entering An Integer Number for Process! ");
        }
    }
}
