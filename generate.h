#pragma once
#ifndef GENERATE_H
#define GENERATE_H

#include <iostream>
#include <vector>
#include <random>

std::vector<int> generate(int n, int low, int high) {
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<int> dist(low, high);

    std::vector<int> result;
    for (int i = 0; i < n; i++) {
        result.push_back(dist(gen));
    }

    return result;
}

std::vector<int> constant(int n) {

    std::vector<int> result;
    int num = rand() % 1000 + 1;

    for (int i = 0; i < n; i++) {
        result.push_back(num);
    }

    return result;
}

std::vector<int> rising(int n, int low , int high) {


    std::random_device rd;
    std::mt19937 gen(rd());  // seed the generator with a random device

    std::vector<int> result;
    for (int i = 0; i < n; i++) {
        std::uniform_int_distribution<> distrib(low, high);  // create a distribution over [low, high]
        result.push_back(low);  // add the current highest number to the result vector
        low = distrib(gen);  // generate a new random number to be the highest number for the next iteration
    }

    return result;

}

std::vector<int> falling(int n, int high, int low) {

    std::random_device rd;
    std::mt19937 gen(rd());  // seed the generator with a random device

    std::vector<int> result;
    for (int i = 0; i < n; i++) {
        std::uniform_int_distribution<> distrib(low, high);  // create a distribution over [low, high]
        result.push_back(high);  // add the current highest number to the result vector
        high = distrib(gen);  // generate a new random number to be the highest number for the next iteration
    }

    return result;
}



#endif // !GENERATE_H

