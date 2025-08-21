use std::io;

fn main() {
    println!("Welcome to Rust Calculator!");

    // Get first number
    let num1 = read_number("Enter the first number: ");

    // Get second number
    let num2 = read_number("Enter the second number: ");

    // Choose operation
    println!("Choose operation: +  -  *  /");
    let mut op = String::new();
    io::stdin()
        .read_line(&mut op)
        .expect("Failed to read line");
    let op = op.trim();

    // Calculate
    let result = match op {
        "+" => num1 + num2,
        "-" => num1 - num2,
        "*" => num1 * num2,
        "/" => {
            if num2 == 0.0 {
                println!("Cannot divide by zero!");
                return;
            } else {
                num1 / num2
            }
        }
        _ => {
            println!("Invalid operator!");
            return;
        }
    };

    println!("Result: {}", result);
}

fn read_number(prompt: &str) -> f64 {
    loop {
        println!("{}", prompt);
        let mut input = String::new();
        io::stdin()
            .read_line(&mut input)
            .expect("Failed to read line");

        match input.trim().parse::<f64>() {
            Ok(num) => return num,
            Err(_) => println!("Please enter a valid number."),
        }
    }
}
