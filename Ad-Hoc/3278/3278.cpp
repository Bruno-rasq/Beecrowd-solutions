#include <iostream>
#include <string>

using namespace std;

struct Train_obj
{
    long long amount_passengers = 0;
    long long total_capacity;

    Train_obj(long long capacity) : total_capacity(capacity) {}
};

int main()
{
    string output = "possible\n";

    long long capacity, station_stops;
    long long left_train, entered_train, stay_at_station;

    cin >> capacity >> station_stops;

    Train_obj train(capacity);

    for (long long i = 0; i < station_stops; i++)
    {
        cin >> left_train >> entered_train >> stay_at_station;

        // 1) Pessoas saem
        train.amount_passengers -= left_train;

        bool negativePassengers =
            (train.amount_passengers < 0);

        // Estado após saída (momento correto para avaliar vagas)
        long long freeSeats =
            train.total_capacity - train.amount_passengers;

        // 2) Pessoas entram
        train.amount_passengers += entered_train;

        bool capacityExceeded =
            (train.amount_passengers > train.total_capacity);

        // 3) Pessoas ficaram esperando sem necessidade
        bool waitedInVain =
            (stay_at_station > 0 && freeSeats > entered_train);

        // 4) Última estação não pode ter espera
        bool waitingAtLastStation =
            (i == station_stops - 1 && stay_at_station > 0);

        if (negativePassengers ||
            capacityExceeded ||
            waitedInVain ||
            waitingAtLastStation)
        {
            output = "impossible\n";
            break;
        }
    }

    // Trem deve terminar vazio
    if (train.amount_passengers != 0)
        output = "impossible\n";

    cout << output;
}