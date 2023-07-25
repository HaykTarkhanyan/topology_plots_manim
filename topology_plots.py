from manim import *
from scipy.spatial.distance import euclidean

class Id24(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        # Set everything else to black
        # self.
        # Add 2D plane
        plane = NumberPlane()
        # self.add(plane)    
        
        square = Square().set_color(color=BLACK)
        self.add(square)
        
        # Add labels to the square
        print(square.get_left())
        
        label_a = MathTex("A").next_to(np.array([-1, -1, 0]), DL*0.2).set_color(color=BLACK)
        label_b = MathTex("B").next_to(np.array([-1, 1, 0]), UL*0.2).set_color(color=BLACK)
        label_c = MathTex("C").next_to(np.array([1, 1, 0]), UR*0.2).set_color(color=BLACK)
        label_d = MathTex("D").next_to(np.array([1, -1, 0]), DR*0.2).set_color(color=BLACK)
        self.add(label_a, label_b, label_c, label_d)
        
        # add 10 equally spaced vertical lines in the square
        lines = VGroup(*[Line(square.get_left() + DOWN + (square.get_width()/11)*i*RIGHT, square.get_left() + DOWN + (square.get_width()/11)*i*RIGHT + square.get_height()*UP).set_color(color=BLACK) for i in range(1, 11)])
        self.add(lines)
        
        
        circle = Circle().shift(RIGHT*4).set_color(BLACK)
        self.add(circle)
        
        # add a point on the circle centered at the origin
        self.add(Dot(circle.get_center()).scale(0.8).set_color(color=BLACK))
        
        # add equally spaced vertical lines passing through the circle
        num_lines = 10
        def get_vertical_points_on_circle(line, radius, num_pairs):
            center = (line[1] + line[0]) / 2
            
            points_on_perimeter = np.linspace(line[0], line[1], num_pairs)
            
            print(points_on_perimeter)
            pairs = []
            for point in points_on_perimeter:
                horizontal_distance_from_center = euclidean(point, center)
                
                vertical_distance = np.sqrt(radius**2 - horizontal_distance_from_center**2)
                # print("point", point)
                # print("hor dist", horizontal_distance_from_center)
                # print("vertical dist", vertical_distance)
                pairs.append([point + UP*vertical_distance,
                              point - UP*vertical_distance])
            # print(pairs)
            return pairs[1:-1]
            
        points = (get_vertical_points_on_circle([circle.get_left(), circle.get_right()], \
            circle.get_width()/2, 11))
        
        for pair in points:
            self.add(Line(pair[0], pair[1]).set_color(color=BLACK))
        

        # add point and 
        
        aliq = MathTex("\sim").scale(2).shift(RIGHT*2).set_color(color=BLACK)
        self.add(aliq)
        
        def find_point_on_circle_with_given_x_cord(x_cord, center, radius):
            y_cord = np.sqrt(radius**2 - (x_cord - center[0])**2)
            return np.array([x_cord, y_cord, 0])
        
        
        def add_point_and_opposite(letter, cord, move_upper, move_lower):            
            point = find_point_on_circle_with_given_x_cord(cord, circle.get_center(), circle.get_width()/2)
            point_opposite = circle.get_center() - (point - circle.get_center())
            
            label = MathTex(letter).next_to(point, move_upper).set_color(color=BLACK)
            label_opposite = MathTex(letter).next_to(point_opposite, move_lower).set_color(color=BLACK)
            
            self.add(Dot(point).scale(0.8).set_color(color=BLACK))
            self.add(Dot(point_opposite).scale(0.8).set_color(color=BLACK))
            self.add(label)
            self.add(label_opposite)
        
        add_point_and_opposite("A", circle.get_center()[0] + 0.7, UP*0.7, DOWN*0.7 + LEFT*0.1)
        add_point_and_opposite("B", circle.get_center()[0] - 0.6, UL*0.2, DR*0.2)
        add_point_and_opposite("E?", circle.get_center()[0] - 0.1, UP*0.5, DOWN*0.5)
        add_point_and_opposite("D", circle.get_center()[0] + 0.95, RIGHT*0.3 + UP*0.1, LEFT*0.3 + DOWN*0.1)
        
        
        
        
        self.play(Write(Text("a").shift(UP*10)))
           