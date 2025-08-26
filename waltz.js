// "ameliewaltz.js" - adapted by @Ottitsch
// @version 1.2

setDefaultVoicings('legacy')
// drive everything at 64 CPM → 64/60 ≈ 1.0667 cps
setcps(64/60)

stack(
  // Harmonica voice 1 (backing, quieter)
  n("[0@2 ~, ~ [[1,2,3] ~]!2]")
    .chord("<[Dm Am]!2 [F C]!2>/4")
    .anchor("<[B3 G3]!2 [C4 B3]!2>/4")
    .voicing()
    .velocity(0.4)
    .s("gm_piano"),


  // Piano voice (foreground, same melody, full volume)
  n("<[3@5.5 2@0.5 1@3 0@3] [3@3.5 [4 3 2 1 2]@2.5 1@3 0@3] [2@5.5 1@0.5 -3@6]!2>/4")
    .scale("a5:minor")
    .velocity(0.6)
    .s("gm_piano")
)
// global mix
.clip(1)
.attack(0.1)
.release(0.1)
.room(1.5)
.gain(1.0)
.pianoroll()

