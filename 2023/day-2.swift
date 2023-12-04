import Foundation

let url = URL(filePath: "input-2.txt")
let text = try! String(contentsOf: url)
let lines = text.components(separatedBy: "\n")

// Part 1

enum Color: String {
  case red, green, blue
}

let maxCubes: [Color: Int] = [
  .red: 12,
  .green: 13,
  .blue: 14,
]

func isValidDraw(_ draw: String) -> Bool {
  if let (num, color) = parseDraw(draw) {
    return num <= maxCubes[color]!
  }
  return false
}

func parseDraw(_ draw: String) -> (Int, Color)? {
  let regex = #/(\d+) (red|green|blue)/#
  if let match = draw.firstMatch(of: regex) {
    let num = Int(match.1)!
    if let color = Color(rawValue: String(match.2)) {
      return (num, color)
    }
  }
  return nil
}

var result = 0

gameLoop: for line in lines {
  guard line != "" else {
    break
  }

  let regex = #/Game (\d+): (.*)/#
  if let match = line.firstMatch(of: regex) {
    let gameId = Int(match.1)!
    let draws = match.2.split(separator: ";")
    for draw in draws {
      let drawColors = draw.split(separator: ", ")
      for drawColor in drawColors {
        if !isValidDraw(String(drawColor)) {
          continue gameLoop
        }
      }
    }
    result += gameId
  }
}

print("Part 1: \(result)")


// Part 2

result = 0

for line in lines {
  guard line != "" else {
    break
  }

  let regex = #/Game (\d+): (.*)/#
  if let match = line.firstMatch(of: regex) {
    let draws = match.2.split(separator: ";")
    var minCubes: [Color: Int] = [.red: 0, .green: 0, .blue: 0]
    for draw in draws {
      let drawColors = draw.split(separator: ", ")
      for drawColor in drawColors {
        if let (num, color) = parseDraw(String(drawColor)) {
          minCubes[color] = max(num, minCubes[color]!)
        }
      }
    }
    result += minCubes[.red]! * minCubes[.green]! * minCubes[.blue]!
  }
}

print("Part 2: \(result)")
