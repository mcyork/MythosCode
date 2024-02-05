enum TianShen {
    YuHuangDaDi,
    SunWuKong,
    ChangE,
}

fn tongzhi(tianshen: TianShen) -> &'static str {
    match tianshen {
        TianShen::YuHuangDaDi => "玉皇大帝以智慧和正义统治着天地。",
        TianShen::SunWuKong => "孙悟空，齐天大圣，在天庭制造了不少麻烦。",
        TianShen::ChangE => "嫦娥，月亮女神，照亮了夜空。",
    }
}

fn main() {
    println!("{}", tongzhi(TianShen::YuHuangDaDi));
    println!("{}", tongzhi(TianShen::SunWuKong));
    println!("{}", tongzhi(TianShen::ChangE));
}
