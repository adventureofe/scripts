;; tictactoe.el -- play tic tac toe in emacs

(defun tic-tac-toe ()
    "start playing tic tac toe"
    (interactive) ;; lets M-x tic-tac-toe work
    (switch-to-buffer "tictactoe") ;;switch to buffer or create
    (tictactoe-mode)
    (tictactoe-init)
)

(define-derived-mode tictactoe-mode special-mode "tic-tac-toe")

(defun tictactoe-init ()
  "start a new game of tic tac toe"
  (setq *tictactoe-board* (make-vector (* *tictactoe-size*
                                          *tictactoe-size*) ?\.))
  (tictactoe-print-board)
)

(defvar *tictactoe-board* nil
  "The board itself")

(defconst *tictactoe-size* 3
  "the size of the board -- both height and width.")


(tic-tac-toe)


(defun tictactoe-print-board ()
  (let ((inhibit-read-only t))
    (erase-buffer)
    (dotimes (row *tictactoe-size*)
      (dotimes (column *tictactoe-size*)
        (insert (tictactoe-get-sqaure row column))))))


(defun tictactoe-get-square (row column)
  "get the value in the row, column square"
  (elt *tictactoe-board*
       (+ column
          (* row
             *tictactoe-size*))))
