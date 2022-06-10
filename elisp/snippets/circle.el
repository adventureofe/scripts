;; area - circumfernece - radius
(defun circle-area-given-radius (radius)
  (* pi (expt radius 2)))

(defun circle-area-given-circumference (circumference)
  (/ (expt circumference 2) (* 4 pi)))

(defun circle-radius-given-area (area)
  (sqrt (/ area pi)))

(defun circle-radius-given-circumference (circumference)
  (/ (/ circumference pi) 2))

(defun circle-circumference-given-radius(radius)
  (* 2 pi radius))

(defun circle-circumference-given-area (area)
  (* 2 (sqrt (* pi area))))

;; annulus
(defun annulus-area-given-radii(inner-radius outer-radius)
  (* pi (- (expt outer-radius 2) (expt inner-radius 2))))

