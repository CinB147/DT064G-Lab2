#include <iostream>
#include <ctime>
#include <chrono>
#include <numeric>
#include <fstream>
#include "sort.h"
#include "generate.h"

enum token {
    Random , Constant , Rising , Falling
};

double calSD(const std::vector<double>& durations, double mean) {

    double sq_sum = std::inner_product(durations.begin(), durations.end(), durations.begin(), 0.0,[](double const& x, double const& y) { return x + y; },
        [mean](double const& x, double const& y) { return (x - mean) * (y - mean); });
    return std::sqrt(sq_sum / durations.size());
 
}
//double calculateStandardDeviation(const std::vector<double>& durations, double mean, int samples) {
//    double variance = 0.0;
//
//    for (const double& duration : durations) {
//        variance += pow(duration - mean, 2);
//    }
//
//    variance /= samples;
//    double standardDeviation = sqrt(variance);
//
//    return standardDeviation;
//}

void run(token t, int n) {
    int size = 16000;
    int samples = 10;
    std::string name;
    std::string tname;

    std::vector<int> myvec;
    double duration;
    std::vector<double> result;

    double mean;

    for (int i = 0; i < 1; i++)
    {
        for (int j = 0; j < samples; j++) {

            switch (t) {
            case Random:
                myvec = generate(size, 1, 100000); //size of 10 , from 1 to 100
                break;
            case Constant:
                myvec = constant(size); //size of 10 , from 1 to 100
                break;
            case Rising:
                myvec = rising(size, 1, 100000); //size of 10 , from 1 to 100
                break;
            case Falling:
                myvec = falling(size, 100000, 1); //size of 10 , from 1 to 100
                break;
            }

            auto start = std::chrono::steady_clock::now();
            switch (n)
            {
            case 1:
                insertionsort(myvec);
                name = "Insertionsort";
                break;
            case 2:
                selectionSort(myvec);
                name = "SelectionSort";
                break;

            case 3:
                quickSort(myvec, 0, myvec.size() - 1);
                /*for (const auto& value : myvec) {
                    std::cout << value << " ";
                }
                std::cout << std::endl;*/
                name = "QuickSort";
                break;

            case 4:
                quickSortm3(myvec, 0, myvec.size() - 1);
                name = "Quicksort median-of-three";
                break;
            case 5:
                std::sort(myvec.begin(), myvec.end());
                name = "std::sort";
                break;


            default:
                break;
            }
            auto end = std::chrono::steady_clock::now();
            auto Timer = std::chrono::duration<double,std::milli> (end - start);
            duration = Timer.count();
            result.push_back(duration);
        }

    }
    if (t == 0) tname = "Randomnumber";
    if (t == 1) tname = "Constantnumber";
    if (t == 2) tname = "Risingnumber";
    if (t == 3) tname = "Fallingnumber";
    double sum = std::accumulate(result.begin(), result.end(), 0.0);
    mean = sum / result.size();;
    std::cout << name << " Avarge Timer takes : " << mean << " ms. As " << tname << "\n";

    double standardDeviation = calSD(result, mean);
    std::cout << "Standard Deviation: " << standardDeviation << std::endl;


    std::ofstream ofile;

    switch (n)
    {
    case 1: 
        if (t == Random) {
            ofile.open("SortAlgoritm/Insertionsort/Random.txt", std::fstream::app);
            ofile << size << "\t" << mean << "\t" << standardDeviation << "\t" << samples << "\t\n";
            break;
        }
        else if (t == Constant) {
            ofile.open("SortAlgoritm/Insertionsort/Constant.txt", std::fstream::app);
            ofile << size << "\t" << mean << "\t" << standardDeviation << "\t" << samples << "\t\n";
            break;
        }
        else if (t == Rising) {
            ofile.open("SortAlgoritm/Insertionsort/Rising.txt", std::fstream::app);
            ofile << size << "\t" << mean << "\t" << standardDeviation << "\t" << samples << "\t\n";
            break;
        }
        else if (t == Falling) {
            ofile.open("SortAlgoritm/Insertionsort/Falling.txt", std::fstream::app);
            ofile << size << "\t" << mean << "\t" << standardDeviation << "\t" << samples << "\t\n";
            break;
        }
    case 2:
        if (t == Random) {
            ofile.open("SortAlgoritm/SelectionSort/Random.txt", std::fstream::app);
            ofile << size << "\t" << mean << "\t" << standardDeviation << "\t" << samples << "\t\n";
            break;
        }
        else if (t == Constant) {
            ofile.open("SortAlgoritm/SelectionSort/Constant.txt", std::fstream::app);
            ofile << size << "\t" << mean << "\t" << standardDeviation << "\t" << samples << "\t\n";
            break;
        }
        else if (t == Rising) {
            ofile.open("SortAlgoritm/SelectionSort/Rising.txt", std::fstream::app);
            ofile << size << "\t" << mean << "\t" << standardDeviation << "\t" << samples << "\t\n";
            break;
        }
        else if (t == Falling) {
            ofile.open("SortAlgoritm/SelectionSort/Falling.txt", std::fstream::app);
            ofile << size << "\t" << mean << "\t" << standardDeviation << "\t" << samples << "\t\n";
            break;
        }
    case 3:
        if (t == Random) {
            ofile.open("SortAlgoritm/QuickSort/Random.txt", std::fstream::app);
            ofile << size << "\t" << mean << "\t" << standardDeviation << "\t" << samples << "\t\n";
            break;
        }
        else if (t == Constant) {
            ofile.open("SortAlgoritm/QuickSort/Constant.txt", std::fstream::app);
            ofile << size << "\t" << mean << "\t" << standardDeviation << "\t" << samples << "\t\n";
            break;
        }
        else if (t == Rising) {
            ofile.open("SortAlgoritm/QuickSort/Rising.txt", std::fstream::app);
            ofile << size << "\t" << mean << "\t" << standardDeviation << "\t" << samples << "\t\n";
            break;
        }
        else if (t == Falling) {
            ofile.open("SortAlgoritm/QuickSort/Falling.txt", std::fstream::app);
            ofile << size << "\t" << mean << "\t" << standardDeviation << "\t" << samples << "\t\n";
            break;
        }
    case 4:
        if (t == Random) {
            ofile.open("SortAlgoritm/Quicksort median-of-three/Random.txt", std::fstream::app);
            ofile << size << "\t" << mean << "\t" << standardDeviation << "\t" << samples << "\t\n";
            break;
        }
        else if (t == Constant) {
            ofile.open("SortAlgoritm/Quicksort median-of-three/Constant.txt", std::fstream::app);
            ofile << size << "\t" << mean << "\t" << standardDeviation << "\t" << samples << "\t\n";
            break;
        }
        else if (t == Rising) {
            ofile.open("SortAlgoritm/Quicksort median-of-three/Rising.txt", std::fstream::app);
            ofile << size << "\t" << mean << "\t" << standardDeviation << "\t" << samples << "\t\n";
            break;
        }
        else if (t == Falling) {
            ofile.open("SortAlgoritm/Quicksort median-of-three/Falling.txt", std::fstream::app);
            ofile << size << "\t" << mean << "\t" << standardDeviation << "\t" << samples << "\t\n";
            break;
        }
    case 5:
        if (t == Random) {
            ofile.open("SortAlgoritm/std_sort/Random.txt", std::fstream::app);
            ofile << size << "\t" << mean << "\t" << standardDeviation << "\t" << samples << "\t\n";
            break;
        }
        else if (t == Constant) {
            ofile.open("SortAlgoritm/std_sort/Constant.txt", std::fstream::app);
            ofile << size << "\t" << mean << "\t" << standardDeviation << "\t" << samples << "\t\n";
            break;
        }
        else if (t == Rising) {
            ofile.open("SortAlgoritm/std_sort/Rising.txt", std::fstream::app);
            ofile << size << "\t" << mean << "\t" << standardDeviation << "\t" << samples << "\t\n";
            break;
        }
        else if (t == Falling) {
            ofile.open("SortAlgoritm/std_sort/Falling.txt", std::fstream::app);
            ofile << size << "\t" << mean << "\t" << standardDeviation << "\t" << samples << "\t\n";
            break;
        }
    default:
        break;
    }
}

void print() {

}

int main() {

    while (true) {
        int input;

        std::cout << "Lab 2 : Analys av sorteringsalgoritmer \n";
        std::cout << "[1] Insertionsort \n";
        std::cout << "[2] SelectionSort \n";
        std::cout << "[3] QuickSort \n";
        std::cout << "[4] Quicksort median-of-three \n";
        std::cout << "[5] std::sort \n";
        std::cout << "[0] Exit \n";
        std::cout << "Enter: ";
        std::cin >> input;
        switch (input) {
        case 1:
            system("cls");
            std::cout << " ------------------------------------------\n";
            std::cout << "|              Insertionsort               |\n";
            std::cout << " ------------------------------------------\n";
            run(Random, 1);
            run(Constant, 1);
            run(Rising, 1);
            run(Falling, 1);
            break;
        case 2:
            system("cls");
            std::cout << " ------------------------------------------\n";
            std::cout << "|              SelectionSort               |\n";
            std::cout << " ------------------------------------------\n";
            run(Random, 2);
            run(Constant, 2);
            run(Rising, 2);
            run(Falling, 2);
            break;
        case 3:
            system("cls");
            std::cout << " ------------------------------------------\n";
            std::cout << "|                 QuickSort                |\n";
            std::cout << " ------------------------------------------\n";
            run(Random, 3);
            run(Constant, 3);
            run(Rising, 3);
            run(Falling, 3);
            break;
        case 4:
            system("cls");
            std::cout << " ------------------------------------------\n";
            std::cout << "|       Quicksort median-of-three         |\n";
            std::cout << " ------------------------------------------\n";
            run(Random, 4);
            run(Constant, 4);
            run(Rising, 4);
            run(Falling, 4);
            break;
        case 5:
            system("cls");
            std::cout << " ------------------------------------------\n";
            std::cout << "|                 std::sort                |\n";
            std::cout << " ------------------------------------------\n";

            run(Random, 5);
            run(Constant, 5);
            run(Rising, 5);
            run(Falling, 5);
            break;

        case 0:
            std::cout << "Bye!\n";
            exit(1);

        default:
            std::cout << "Invalid!\n";
            break;
        }
    

    }


}
