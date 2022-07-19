;; random
;;emacs always starts with same random seed every startup

;; psuedo random between 0-9
(random 10)

;; psuedo random between 1-10
(+ (random 10) 1)

;; seeded random number from time/date
(random t)

;; function for ranged random
(defun random-in-range (min max)
  (+ min (random (+ 1 (- max min)))))


(random-in-range 1 10)
