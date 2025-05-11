#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <thread>
#include <future>
#include <mutex>
#include <regex>
#include <memory>
#include <chrono>

std::mutex mtx;

int main() {
    using namespace std::chrono_literals;

    // <string>, <iostream>
    std::string input = "Hello123 C++ World456!";
    std::cout << "Original input: " << input << std::endl;

    // <regex>
    std::regex pattern(R"(\d+)");
    std::string cleaned = std::regex_replace(input, pattern, "");
    std::cout << "Cleaned input (numbers removed): " << cleaned << std::endl;

    // <vector>, <memory>
    std::vector<std::shared_ptr<std::string>> words;
    std::istringstream iss(cleaned);
    std::string word;
    while (iss >> word) {
        words.push_back(std::make_shared<std::string>(word));
    }

    // <fstream>
    std::ofstream file("output.txt");
    for (const auto& w : words) {
        file << *w << '\n';
    }
    file.close();

    // <thread>, <mutex>, <chrono>, <future>
    auto async_task = std::async(std::launch::async, []() {
        std::this_thread::sleep_for(1s); // wait 1 second
        std::lock_guard<std::mutex> lock(mtx);
        std::cout << "Async task completed after 1 second." << std::endl;
        return 42;
    });

    int result = async_task.get();
    std::cout << "Async result: " << result << std::endl;

    return 0;
}