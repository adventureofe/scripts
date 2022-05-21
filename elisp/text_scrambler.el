(defun replace-char(char alphabet replacements)
  (when (string= char alphabet)
    (nth replacements 1)))


(defun text-scrambler (text)
  (interactive)
  (let ((alphabet '("a" "b" "c" "d"))
        (replacements '("α" "в" "ℂ" "𝕯"))
)
  
  ;; (mapcar (lambda (c) (char-to-string c)) text))
  (mapcar (lambda (a) (equal a (mapcar (lambda (c) (identity c)) text))) alphabet)
  )
)

(text-scrambler "aaa")
