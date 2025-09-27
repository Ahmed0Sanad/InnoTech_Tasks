using System.Diagnostics;
using System.Text;


Console.Write("Hello, Please enter the maximum number you need to write: ");


string? maximumNumberFromUser;
maximumNumberFromUser = Console.ReadLine();

int maximumNumber;
while (string.IsNullOrWhiteSpace(maximumNumberFromUser) || !int.TryParse(maximumNumberFromUser, out maximumNumber) || maximumNumber <= 0)
{
    Console.WriteLine("Invalid input. Please enter a positive integer: ");
    maximumNumberFromUser = Console.ReadLine();
}

string numbers;
numbers = string.Empty;


Stopwatch stopwatch = new Stopwatch();
stopwatch.Start();


for (int i = 1; i <= maximumNumber; i++)
    numbers = $"{numbers}{i}{(i != maximumNumber ? "," : "")}";

stopwatch.Stop();
var StringApproachTime = stopwatch.Elapsed.TotalMilliseconds;

stopwatch.Reset();
stopwatch.Start();
StringBuilder numbersNewApproach = new();

for (int i = 1; i <= maximumNumber; i++)
    numbersNewApproach.Append($"{i}{(i != maximumNumber? "," : "")}");

stopwatch.Stop();
var StringBuilderApproachTime = stopwatch.Elapsed.TotalMilliseconds;

Console.WriteLine(numbers);
Console.WriteLine($"Using String class, Elapsed Time = {StringApproachTime}");
Console.WriteLine(numbersNewApproach);
Console.WriteLine($"Using StringBuilder class, Elapsed Time = {StringBuilderApproachTime}");