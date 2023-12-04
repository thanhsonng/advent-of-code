import Foundation

let url = URL(filePath: "input-1.txt")
let text = try! String(contentsOf: url)
let lines = text.components(separatedBy: "\n")

var result = 0

for line in lines {
  guard line != "" else {
    break
  }
  // Left pointer
  var left = line.startIndex
  while left < line.endIndex && !line[left].isNumber {
    left = line.index(after: left)
  }
  let digit1 = left < line.endIndex ? line[left] : "0"

  // Right pointer
  var right = line.index(before: line.endIndex)
  while right > line.startIndex && !line[right].isNumber {
    right = line.index(before: right)
  }
  let digit2 = right >= line.startIndex ? line[right] : "0"

  // Combine
  let num = Int("\(digit1)\(digit2)") ?? 0
  result += num
}

print("Part 1: \(result)")

result = 0
let numbers: [String: Character] = [
  "one": "1",
  "two": "2",
  "three": "3",
  "four": "4",
  "five": "5",
  "six": "6",
  "seven": "7",
  "eight": "8",
  "nine": "9",
]

for line in lines {
  guard line != "" else {
    break
  }

  var wordIndices: [(Character, String.Index)] = []
  for (word, num) in numbers {
    let regex = try Regex(word)
    line.ranges(of: regex).forEach { (range) -> Void in
      wordIndices.append((num, range.lowerBound))
    }
  }
  wordIndices.sort { $0.1 < $1.1 }

  // Left pointer
  var left = line.startIndex
  while left < line.endIndex && !line[left].isNumber {
    left = line.index(after: left)
  }
  let digit1: Character = if let first = wordIndices.first {
    left < first.1 ? line[left] : first.0
  } else {
    left < line.endIndex ? line[left] : "0"
  }

  // Right pointer
  var right = line.index(before: line.endIndex)
  while right > line.startIndex && !line[right].isNumber {
    right = line.index(before: right)
  }
  let digit2: Character = if let last = wordIndices.last {
    right > last.1 ? line[right] : last.0
  } else {
    right >= line.startIndex ? line[right] : "0"
  }

  // Combine
  let num = Int("\(digit1)\(digit2)") ?? 0
  result += num
}

print("Part 2: \(result)")
