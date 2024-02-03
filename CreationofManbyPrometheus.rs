enum Creation {
    Man,
    Punishment,
}

fn prometheus_creates(creation: Creation) -> &'static str {
    use Creation::*;

    match creation {
        Man => "Prometheus creates man from clay.",
        Punishment => "Prometheus is punished for his gift to mankind.",
    }
}

fn main() {
    println!("{}", prometheus_creates(Creation::Man));
    println!("{}", prometheus_creates(Creation::Punishment));
}
