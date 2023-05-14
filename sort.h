#pragma once
#ifndef SORT_H
#define SORT_H
#include <iostream>
#include <algorithm>
#include <vector>
#include <stack>

//--------INSERTION---------//
template<typename T>
void insertionsort(std::vector<T>& myvec) {
    for (int i = 1; i < myvec.size(); ++i) {
        T num = myvec[i];
        int j = i - 1;

        // Use binary search to find the correct position to insert the element
        int pos = std::upper_bound(myvec.begin(), myvec.begin() + i, num) - myvec.begin();

        // Shift elements to the right
        for (; j >= pos; --j) {
            myvec[j + 1] = myvec[j];
        }

        // Insert the element at the correct position
        myvec[j + 1] = num;
    }
}

//-----------SELECTION----------//
template<typename T>
void selectionSort(std::vector<T>& myvec) {
    for (auto it = myvec.begin(); it != myvec.end() - 1; ++it) {
        auto minIt = std::min_element(it, myvec.end());
        std::iter_swap(it, minIt);
    }
}


//-------QUICK-----//
template<typename T>
void swap(T& a, T& b) {
    T temp = a;
    a = b;
    b = temp;
}

template<typename T>
int partition(std::vector<T>& myvec, int low, int high) {
    T pivot = myvec[high];
    int i = low - 1;

    for (int j = low; j <= high - 1; j++) {
        if (myvec[j] < pivot) {
            i++;
            swap(myvec[i], myvec[j]);
        }
    }
    swap(myvec[i + 1], myvec[high]);

    return i + 1;
}

template<typename T>
void quickSort(std::vector<T>& myvec, int low, int high) {
    std::stack<std::pair<int, int>> stack;
    stack.push(std::make_pair(low, high));

    while (!stack.empty()) {
        low = stack.top().first;
        high = stack.top().second;
        stack.pop();

        int pivotIndex = partition(myvec, low, high);

        if (pivotIndex - 1 > low)
            stack.push(std::make_pair(low, pivotIndex - 1));

        if (pivotIndex + 1 < high)
            stack.push(std::make_pair(pivotIndex + 1, high));
    }
}


//-------QUICKmedianOfThree-----//


template<typename T>
int medianOfThree(std::vector<T>& myvec, int low, int high) {
    int mid = low + (high - low) / 2;

    if (myvec[low] > myvec[mid])
        swap(myvec[low], myvec[mid]);

    if (myvec[low] > myvec[high])
        swap(myvec[low], myvec[high]);

    if (myvec[mid] > myvec[high])
        swap(myvec[mid], myvec[high]);

    return mid;
}

template<typename T>
int partition3(std::vector<T>& myvec, int low, int high) {
    //finding pivot mid index
    int pivotIndex = medianOfThree(myvec, low, high);
    T pivot = myvec[pivotIndex];
    int i = low - 1;

    swap(myvec[pivotIndex], myvec[high]);

    for (int j = low; j <= high - 1; j++) {
        if (myvec[j] < pivot) {
            i++;
            swap(myvec[i], myvec[j]);
        }
    }
    swap(myvec[i + 1], myvec[high]);

    return i + 1;
}

template<typename T>
void quickSortm3(std::vector<T>& myvec, int low, int high) {
    std::stack<std::pair<int, int>> stack;
    stack.push(std::make_pair(low, high));

    while (!stack.empty()) {
        low = stack.top().first;
        high = stack.top().second;
        stack.pop();

        int pivotIndex = partition3(myvec, low, high);

        if (pivotIndex - 1 > low)
            stack.push(std::make_pair(low, pivotIndex - 1));

        if (pivotIndex + 1 < high)
            stack.push(std::make_pair(pivotIndex + 1, high));
    }
}

#endif // !SORT_H
