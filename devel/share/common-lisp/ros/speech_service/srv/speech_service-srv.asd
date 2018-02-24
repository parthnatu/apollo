
(cl:in-package :asdf)

(defsystem "speech_service-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "ReturnDetectedSpeech" :depends-on ("_package_ReturnDetectedSpeech"))
    (:file "_package_ReturnDetectedSpeech" :depends-on ("_package"))
  ))