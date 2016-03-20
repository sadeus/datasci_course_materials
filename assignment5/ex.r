library('ggplot2')
library('rpart')
library('randomForest')
library('e1071')
theme_set(theme_bw())
setwd("d:/sebas/coursera/datasci_course_materials/assignment5/")

#Obtengo los datos
data <- read.csv("seaflow_21min.csv")
#data <- data[data$file_id != 208, ]

#Bootstraping, con reemplazo

#Creo los valores de prueba. length(train) = length(data)/2
train <- data[sample(nrow(data), floor(nrow(data)[1]/2)),]

#Creo los valores de testeo. length(test) = length(data)/2
test <- data[sample(nrow(data), floor(nrow(data)[1]/2)), ]

#Mantengo los valores objetivos del test, para observar la precisión del clasificador
testObj <- factor(test$pop)

#Le saco los valores objetivos
test <- test[, - which(names(test) %in% c('pop'))]
ggplot(data) + geom_point(aes(x= pe, y = chl_small, colour = pop))

fol <- formula(pop ~ fsc_small + fsc_perp + fsc_big + pe + chl_big + chl_small)


#Predigo con un solo arbol de decisiones
model <- rpart(fol, method="class", data=train)
print(model)
Predicción sobre los datos de testeo. El tipo "vector" devuelve la clase del dato
p <- predict(model, test, type='vector')
#print(table(pred=p, true=testObj))
accuracy <- sum(as.numeric(testObj) == p)/length(p)
print(accuracy)

#Ahora fitteo con Random Forests
model <- randomForest(fol, data=train)
p <- predict(model, test, type='response')
accuracy <- sum(testObj == p)/length(p)
print(table(pred=p, true=testObj))
print(accuracy)
print(importance(model))

#Fitteo con SVM
model <- svm(fol, data=train)
print(model)
p <- predict(model, test)
print(table(pred=p, true=testObj))
accuracy <- sum(testObj == p)/length(p)
print(accuracy)

