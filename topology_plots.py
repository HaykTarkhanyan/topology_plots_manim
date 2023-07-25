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

class Id31(Scene):
    def construct(self):
        line_opacity = 0.4
        self.camera.background_color = WHITE

        plane = NumberPlane()
        # self.add(plane)    
        
        rect = Rectangle(BLACK, 2, 4)#.set_color(color=BLACK)
        self.add(rect)
        
        
        
        lines = VGroup(*[Line(rect.get_left() + DOWN + (rect.get_width()/11)*i*RIGHT, 
                              rect.get_left() + DOWN + (rect.get_width()/11)*i*RIGHT + rect.get_height()*UP)
                         .set_opacity(line_opacity)
                         .set_color(color=BLACK) for i in range(1, 11)])
        self.add(lines)
        
        
        eq1 = MathTex(r"(a,b) \times (c,d)").move_to(rect.get_center()).scale(1.4).set_color(color=BLACK)
        
        # self.add(Rectangle(WHITE, eq1.get_height(), eq1.get_width(), fill_opacity=1).move_to(eq1.get_center()))
        self.add(eq1)
        
        #############################################################
        # right one
        circle = Circle().shift(RIGHT*4).set_color(BLACK)
        self.add(circle)
        
        num_lines = 10
        def get_vertical_points_on_circle(line, radius, num_pairs):
            center = (line[1] + line[0]) / 2
            
            points_on_perimeter = np.linspace(line[0], line[1], num_pairs)
            
            print(points_on_perimeter)
            pairs = []
            for point in points_on_perimeter:
                horizontal_distance_from_center = euclidean(point, center)
                
                vertical_distance = np.sqrt(radius**2 - horizontal_distance_from_center**2)
                pairs.append([point + UP*vertical_distance,
                              point - UP*vertical_distance])

            return pairs[1:-1]
            
        points = (get_vertical_points_on_circle([circle.get_left(), circle.get_right()], \
            circle.get_width()/2, 11))

        for pair in points:
            self.add(Line(pair[0], pair[1]).set_color(color=BLACK).set_opacity(line_opacity))
       
    
        circle_center = Dot(circle.get_center()).scale(0.8).set_color(color=BLACK)
        self.add(circle_center)
        x_label = MathTex("x").next_to(circle_center, DOWN*0.7).set_color(color=BLACK)
        self.add(x_label)
       
        def find_point_on_circle_with_given_x_cord(x_cord, center, radius):
            y_cord = np.sqrt(radius**2 - (x_cord - center[0])**2)
            return np.array([x_cord, y_cord, 0])

        cord = Line(circle.get_center(), 
                    find_point_on_circle_with_given_x_cord(circle.get_center()[0] + 0.7, 
                                                           circle.get_center(), 
                                                           circle.get_width()/2)).set_color(color=BLACK)
        self.add(cord)
        
        r_label = MathTex("r").move_to(cord.get_center()+UP*0.3).set_color(color=BLACK)

        self.add(r_label)
        self.play(Write(Text("a").shift(UP*10)))

