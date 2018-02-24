; Auto-generated. Do not edit!


(cl:in-package speech_service-srv)


;//! \htmlinclude ReturnDetectedSpeech-request.msg.html

(cl:defclass <ReturnDetectedSpeech-request> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass ReturnDetectedSpeech-request (<ReturnDetectedSpeech-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ReturnDetectedSpeech-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ReturnDetectedSpeech-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name speech_service-srv:<ReturnDetectedSpeech-request> is deprecated: use speech_service-srv:ReturnDetectedSpeech-request instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ReturnDetectedSpeech-request>) ostream)
  "Serializes a message object of type '<ReturnDetectedSpeech-request>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ReturnDetectedSpeech-request>) istream)
  "Deserializes a message object of type '<ReturnDetectedSpeech-request>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ReturnDetectedSpeech-request>)))
  "Returns string type for a service object of type '<ReturnDetectedSpeech-request>"
  "speech_service/ReturnDetectedSpeechRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ReturnDetectedSpeech-request)))
  "Returns string type for a service object of type 'ReturnDetectedSpeech-request"
  "speech_service/ReturnDetectedSpeechRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ReturnDetectedSpeech-request>)))
  "Returns md5sum for a message object of type '<ReturnDetectedSpeech-request>"
  "74697ed3d931f6eede8bf3a8dfeca160")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ReturnDetectedSpeech-request)))
  "Returns md5sum for a message object of type 'ReturnDetectedSpeech-request"
  "74697ed3d931f6eede8bf3a8dfeca160")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ReturnDetectedSpeech-request>)))
  "Returns full string definition for message of type '<ReturnDetectedSpeech-request>"
  (cl:format cl:nil "~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ReturnDetectedSpeech-request)))
  "Returns full string definition for message of type 'ReturnDetectedSpeech-request"
  (cl:format cl:nil "~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ReturnDetectedSpeech-request>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ReturnDetectedSpeech-request>))
  "Converts a ROS message object to a list"
  (cl:list 'ReturnDetectedSpeech-request
))
;//! \htmlinclude ReturnDetectedSpeech-response.msg.html

(cl:defclass <ReturnDetectedSpeech-response> (roslisp-msg-protocol:ros-message)
  ((text
    :reader text
    :initarg :text
    :type cl:string
    :initform ""))
)

(cl:defclass ReturnDetectedSpeech-response (<ReturnDetectedSpeech-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ReturnDetectedSpeech-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ReturnDetectedSpeech-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name speech_service-srv:<ReturnDetectedSpeech-response> is deprecated: use speech_service-srv:ReturnDetectedSpeech-response instead.")))

(cl:ensure-generic-function 'text-val :lambda-list '(m))
(cl:defmethod text-val ((m <ReturnDetectedSpeech-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader speech_service-srv:text-val is deprecated.  Use speech_service-srv:text instead.")
  (text m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ReturnDetectedSpeech-response>) ostream)
  "Serializes a message object of type '<ReturnDetectedSpeech-response>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'text))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'text))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ReturnDetectedSpeech-response>) istream)
  "Deserializes a message object of type '<ReturnDetectedSpeech-response>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'text) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'text) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ReturnDetectedSpeech-response>)))
  "Returns string type for a service object of type '<ReturnDetectedSpeech-response>"
  "speech_service/ReturnDetectedSpeechResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ReturnDetectedSpeech-response)))
  "Returns string type for a service object of type 'ReturnDetectedSpeech-response"
  "speech_service/ReturnDetectedSpeechResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ReturnDetectedSpeech-response>)))
  "Returns md5sum for a message object of type '<ReturnDetectedSpeech-response>"
  "74697ed3d931f6eede8bf3a8dfeca160")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ReturnDetectedSpeech-response)))
  "Returns md5sum for a message object of type 'ReturnDetectedSpeech-response"
  "74697ed3d931f6eede8bf3a8dfeca160")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ReturnDetectedSpeech-response>)))
  "Returns full string definition for message of type '<ReturnDetectedSpeech-response>"
  (cl:format cl:nil "string text~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ReturnDetectedSpeech-response)))
  "Returns full string definition for message of type 'ReturnDetectedSpeech-response"
  (cl:format cl:nil "string text~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ReturnDetectedSpeech-response>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'text))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ReturnDetectedSpeech-response>))
  "Converts a ROS message object to a list"
  (cl:list 'ReturnDetectedSpeech-response
    (cl:cons ':text (text msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'ReturnDetectedSpeech)))
  'ReturnDetectedSpeech-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'ReturnDetectedSpeech)))
  'ReturnDetectedSpeech-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ReturnDetectedSpeech)))
  "Returns string type for a service object of type '<ReturnDetectedSpeech>"
  "speech_service/ReturnDetectedSpeech")