sealed class LifeExperience {
    object Joy : LifeExperience()
    object Sorrow : LifeExperience()
    class Learning(val lesson: String) : LifeExperience()
}

fun experienceLife(experience: LifeExperience) {
    when (experience) {
        is LifeExperience.Joy -> println("Embrace the joy.")
        is LifeExperience.Sorrow -> println("Learn from sorrow.")
        is LifeExperience.Learning -> println("Lesson: ${experience.lesson}")
    }
}
