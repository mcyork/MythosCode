fn survival_chance(frog: &str, hours: i32) -> String {
    match frog {
        "persistent_frog" if hours > 5 => "The persistent frog turns the milk into butter and climbs out.".to_string(),
        "quitting_frog" => "The quitting frog gives up and drowns.".to_string(),
        _ => "Unexpected story outcome.".to_string(),
    }
}

fn main() {
    println!("{}", survival_chance("persistent_frog", 6));
    println!("{}", survival_chance("quitting_frog", 3));
}
