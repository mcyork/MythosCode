func path(in life: String?) -> String {
    guard let life = life else { return "Sometimes, the path chooses us." }
    return "Chosen path: \(life)"
}
